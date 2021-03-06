from django.contrib import admin
from system.models import Client, Supplier, ProductOrder, RawOrder, Budget, Product, RawForProduction


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'surname', 'phone', 'created_at', )
    search_fields = ('name', 'surname', 'phone', )


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'surname', 'phone', 'created_at', )
    search_fields = ('name', 'surname', 'phone', )


class ProductOrderAdmin(admin.ModelAdmin):
    def suit_row_attributes(self, obj, request):
        css_class = {
            'SUCCESS': 'success',
            'WAITING': 'warning',
            'FAIL': 'error'
        }
        return {'class': css_class.get(str(obj.status).upper(), 'FAIL')}

    list_display = ('id', 'client', 'product', 'quantity',
                    'total', 'status', 'created_at', )
    search_fields = ('product__name', 'status', )
    autocomplete_fields =['product', 'client']


class RawOrderAdmin(admin.ModelAdmin):
    def suit_row_attributes(self, obj, request):
        css_class = {
            'SUCCESS': 'success',
            'WAITING': 'warning',
            'FAIL': 'error'
        }
        return {'class': css_class.get(str(obj.status).upper(), 'FAIL')}
    list_display = ('id', 'supplier', 'raw', 'quantity',
                    'total', 'status', 'created_at',)
    search_fields = ('raw__name', 'status', )
    autocomplete_fields =['raw', 'supplier']


class DamagedRaw(admin.ModelAdmin):
    def suit_row_attributes(self, obj, request):
        css_class = {
            '0': 'success',
            '1': 'error'
        }
        status = 0 if obj.stock.count > 0 else 1
        return {'class': css_class[str(status)]}

    list_display = ('id', 'stock', 'name', 'created_at',)
    search_fields = ('stock__name', 'name',)
    autocomplete_fields = ['stock']


class DamagedProduct(admin.ModelAdmin):
    def suit_row_attributes(self, obj, request):
        css_class = {
            '0': 'success',
            '1': 'error'
        }
        status = 0 if obj.stock.count > 0 else 1
        return {'class': css_class[str(status)]}

    list_display = ('id', 'stock', 'name', 'created_at',)
    search_fields = ('stock__name', 'name',)
    autocomplete_fields = ['stock']


class RawAdmin(admin.ModelAdmin):
    def suit_row_attributes(self, obj, request):
        css_class = {
            '0': 'success',
            '1': 'error'
        }
        status = 0 if obj.stock.count > 0 else 1
        return {'class': css_class[str(status)]}

    list_display = ('id', 'stock', 'name', 'created_at',)
    search_fields = ('stock__name', 'name',)
    autocomplete_fields = ['stock']


class BudgetAdmin(admin.ModelAdmin):
    def suit_row_attributes(self, obj, request):
        css_class = {
            '0': 'success',
            '1': 'error',
        }
        status = 0 if obj.total_income else 1
        return {'class': css_class[str(status)]}

    list_display = ('id', 'product_order', 'raw_order', 'salaries', 'total_income', 'total_outcome', 'total', 'created_at',
                    'updated_at', )

    search_fields = ('product_order__name', 'raw_order__name')
    autocomplete_fields =['product_order', 'raw_order']


admin.site.register(Client, ClientAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
admin.site.register(RawOrder, RawOrderAdmin)
admin.site.register(Budget, BudgetAdmin)

import coreapi
import coreschema
from rest_framework.schemas import ManualSchema


RegisterSchema = ManualSchema(fields=[
    coreapi.Field(
        'user["name"]',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'user["surname"]',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'user["email"]',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'user["password"]',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'user["password_again"]',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


LoginSchema = ManualSchema(fields=[
    coreapi.Field(
        'email',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'password',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


ProductInfoSchema = ManualSchema(fields=[
    coreapi.Field(
        'product_name',
        required=True,
        location="query",
        schema=coreschema.String()
    ),
])


RawInfoSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw_name',
        required=True,
        location="query",
        schema=coreschema.String()
    ),
])


CreateProductStockSchema = ManualSchema(fields=[
    coreapi.Field(
        'product_stock_name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


CreateRawStockSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw_stock_name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


CreateProductSchema = ManualSchema(fields=[
    coreapi.Field(
        'product_stock_name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'product_name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'quantity',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


CreateRawSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw_stock_name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'raw_name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'quantity',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


CreateClientSchema = ManualSchema(fields=[
    coreapi.Field(
        'email',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'surname',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'phone',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


CreateSupplierSchema = ManualSchema(fields=[
    coreapi.Field(
        'email',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'surname',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'phone',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


CreateProductOrderSchema = ManualSchema(fields=[
    coreapi.Field(
        'client',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'quantity',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


CreateRawOrderSchema = ManualSchema(fields=[
    coreapi.Field(
        'supplier',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
    coreapi.Field(
        'quantity',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])


DamagedCreateRawOrderSchema = ManualSchema(fields=[
    coreapi.Field(
        'raw',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])

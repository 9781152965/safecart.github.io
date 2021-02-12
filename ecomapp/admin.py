from django.contrib import admin
from .models import *


class AdminAdmin(admin.ModelAdmin):
    list_display = ['user','full_name', 'image','mobile']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['user','full_name', 'address','joined_on']

class AdminCategory(admin.ModelAdmin):
    list_display = ['title','slug']

class AdminProduct(admin.ModelAdmin):
    list_display = ['title','image', 'category','selling_price', 'warranty']

class AdminNewProduct(admin.ModelAdmin):
    list_display = ['title','image', 'category','selling_price','warranty']

class AdminProductImage(admin.ModelAdmin):
    list_display = ['product','image']

class AdminCart(admin.ModelAdmin):
    list_display = ['customer','total', 'created_at']

class AdminCartProduct(admin.ModelAdmin):
    list_display = ['cart','product', 'rate','quantity','subtotal']

class AdminOrder(admin.ModelAdmin):
    list_display = ['ordered_by', 'shipping_address','mobile','discount','total','order_status','payment_method','payment_completed']



#admin.site.register(
 #   [Admin, Customer, Category, Product,NewProduct, Cart, CartProduct, Order, ProductImage])


# Register your models here.
admin.site.register(Admin , AdminAdmin)
admin.site.register(Customer , AdminCustomer)
admin.site.register(Category , AdminCategory)
admin.site.register(Product , AdminProduct)
admin.site.register( NewProduct , AdminNewProduct)
admin.site.register( Cart  , AdminCart)
admin.site.register( CartProduct , AdminCartProduct)
admin.site.register(Order , AdminOrder)
admin.site.register(ProductImage , AdminProductImage)
from django.contrib import admin

from shop.models import Brends, Categories, Sneakers, Cart, Reviews


admin.site.register(Sneakers)
admin.site.register(Brends)
admin.site.register(Categories)
admin.site.register(Cart)
admin.site.register(Reviews)

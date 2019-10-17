# -*- coding: utf-8 -*-

"""
    ecommerce URL Configuration
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

if 'rosetta' in settings.INSTALLED_APPS:
     urlpatterns = i18n_patterns(
          path('', include('accounts.urls', namespace='accounts')),
          path(_('cart/'), include('panier.urls', namespace='panier')),
          path(_('orders/'), include('commandes.urls', namespace='commandes')),
          path(_('payment/'), include('payment.urls', namespace='payment')),
          path(_('coupons/'), include('coupons.urls', namespace='coupons')),
          path('', include('shop.urls', namespace='shop')),
          path('rosetta/', include('rosetta.urls')),
          path(_('admin/doc/'), include('django.contrib.admindocs.urls')),
          path('tinymce/', include('tinymce.urls')),
          path(_('admin/'), admin.site.urls),
    )

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.COMPRESS_ROOT, document_root=settings.COMPRESS_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

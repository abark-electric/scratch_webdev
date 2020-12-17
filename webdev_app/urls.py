from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/webdev_app', LeadViewSet, 'webdev_app')

urlpatterns = router.urls


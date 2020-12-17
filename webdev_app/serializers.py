from rest_framework import serializers
from webdev_app.models import Lead


# Making a serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
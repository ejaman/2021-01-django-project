from django.forms import ModelForm
from .models import Order,Inventory


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class itemForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

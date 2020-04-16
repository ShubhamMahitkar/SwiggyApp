from s_admin.models import StateModel, RestaurantTypeModel
from s_admin.models import CityModel
from s_admin.models import AreaModel
from django import forms


class StateForm(forms.ModelForm):
    class Meta:
        model = StateModel
        fields = ('state_name',)


class CityForm(forms.ModelForm):
    class Meta:
        model = CityModel
        fields = "__all__"
        exclude = ('city_no',)


class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = "__all__"
        exclude = ('area_no',)


class RestaurantTypeForm(forms.ModelForm):
    class Meta:
        model = RestaurantTypeModel
        fields = ('type_name',)
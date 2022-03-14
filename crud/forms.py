from django import forms
from .models import DatosGrales

class DatosForm(forms.ModelForm):

	class Meta:
		model = DatosGrales
		fields = ['folio','nombre','confirma','telefono','domicilio',
					'alcaldia','mascota','raza','peso','tiposervicio',
					'fechaingreso','horario','puntual','mensajero',
					'quiencrema','entregaurna','quienentrega','procedencia1','procedencia2',
					'pago','formapago','servicios','tamaño','tipo','mvzrecomienda','comision',
					'eutanasia','tipourna','importadas','huellas','otros','condiciones',
					'fechadeceso','observaciones','capturo']
from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name','last_name','phone',)
        widgets = {
            'first_name': forms.TextInput(
                attrs= {
                    'class': 'classe-a classe-b',
                    'placeholder': 'Escreva aqui'
                }
            )
        }
    
    def clean(self):
        # Para mostrar que a classe tem acesso aos dados dos campos antes da submissão ...
        cleaned_data = self.cleaned_data # Guarda os valores inseridos em um dicionário
        print(cleaned_data)
		# Vamos simular erros
        self.add_error(
			None,
			ValidationError(
				'Dados em falta ou inválidos',
				code='invalid'
			)
		)
        self.add_error(
			None,
			ValidationError(
				'Este campo deve ter no mínimo 10 caracteres',
				code='invalid'
			)
		)
        return super().clean()
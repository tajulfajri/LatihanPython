from django import forms
from django.core import validators

# Custom Validator
# def check_for_a(value):
#     if value[0].lower() != "a":
#         raise forms.ValidationError("Name Needs To Start With a")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Input your email again:") # label is what the user sees
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        vmail = all_clean_data["verify_email"]
        
        if email != vmail:
            raise forms.ValidationError("Make Sure Emails Match!")
    
    # botcatcher = forms.CharField(
    #     required=False,
    #     widget=forms.HiddenInput,
    #     validators=[validators.MaxLengthValidator(0)],
    # )

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

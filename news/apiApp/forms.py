from django import forms

LANGUAGES = [
  ('en', 'en'),
  ('es', 'es'),
  ('fr', ' fr'),
  ('ar', ' ar'),
]


class SearchForm(forms.Form):
  """Search form class

  Args:
      forms (): django forms
  """  
  keyword = forms.CharField(required=True)
  source_category = forms.CharField(required=False)
  language = forms.ChoiceField(choices=LANGUAGES)
  from_date = forms.DateField( input_formats=['%Y-%m-%d'],
  widget=forms.DateInput(format='%yy-%mm-%dd', attrs={'type': 'date'}), required=False)
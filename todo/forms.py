from django import forms

class TodoForm(forms.Form):
	text = forms.CharField(max_length=80,
		widget=forms.TextInput(
			attrs={'classs' : 'form-control', 'placeholder' : 'Enter to e.g. delete junk files', 'aria-label' : 'todo', 'aria-describedby' : 'add-btn'}))
from django.shortcuts import render
from contact.models import Contact

# Create your views here.
def index(request):
    c = Contact.objects.all()
    context = {
        'contacts': c
    }
    return render (
        request,
        'contact/index.html',
        context
    )
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            # Configure email settings
            subject = 'New Contact Form Submission'
            email_message = f'Name: {name}\nPhone Number: {phone_number}\n\n{message}'
            from_email = settings.DEFAULT_FROM_EMAIL

            # Send the email
            send_mail(subject, email_message, from_email, [settings.CONTACT_EMAIL], fail_silently=False)

            return redirect('contact_form/')  # Redirect to the contact form page

    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

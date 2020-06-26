from django.shortcuts import render
from django.http import HttpResponse
from .form import UserForm, TaskInfo
from .models import TaskInfo
from rest_framework.views import APIView    

# Using django rest framework for simplicity 
class show_user(APIView):
    template_name = 'user_info.html'
    temp = 'user_selection.html'

    def get(self, request):
        """
        Function to fetch remove request page
        """
        form = UserForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid:
            user_id = request.POST.get('user_info')
            projects = TaskInfo.objects.filter(id=user_id).values()
            print('projects --> ', projects)
            return render(request, self.temp, {'projects': projects})


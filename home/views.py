from django.views.generic import TemplateView, ListView
from posts.models import Post



class HomeView(TemplateView):
    template_name = 'home/home.html'  # Ensure this matches the template file name
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['breaking_news'] = Post.objects.filter(breaking_news=True).order_by('-created_at')[:4]
        context['other_posts'] = Post.objects.filter(breaking_news=False).order_by('-created_at')[:4]

        return context

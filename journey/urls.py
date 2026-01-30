from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

app_name = 'journey'

urlpatterns = [
        path('', views.post_list, name='post_list'),
        path('post_list', views.post_list, name='post_list'),
        path('signup', views.signup, name='signup'),
        path('post_detail', views.post_detail, name='post_detail'),
        path('post/create/', views.post_new, name='post_new'),
        path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
        path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
        path('comment_list', views.comment_list, name='comment_list'),
        path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
        path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
        path('travelblog_post/<int:post_id>',views.travelblog_post, name='travelblog_post'),
        path(
            'password-reset/',
            auth_views.PasswordResetView.as_view(
                template_name='registration/password_reset_form.html',
                email_template_name='registration/password_reset_email.html',
            ),
            name='password_reset',
        ),
        path(
            'password-reset/done/',
            auth_views.PasswordResetDoneView.as_view(
                template_name='registration/password_reset_done.html',
            ),
            name='password_reset_done',
        ),
        path(
            'reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(
                template_name='registration/password_reset_confirm.html',
            ),
            name='password_reset_confirm',
        ),
        path(
            'reset/done/',
            auth_views.PasswordResetCompleteView.as_view(
                template_name='registration/password_reset_complete.html',
            ),
            name='password_reset_complete',
        ),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()

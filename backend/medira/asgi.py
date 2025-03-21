import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import repair_platform.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startup_project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        URLRouter(repair_platform.routing.websocket_urlpatterns)
    ),
})

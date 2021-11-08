# import os
#
# from django.core.asgi import get_asgi_application
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djecommerce.settings')
#
# application = get_wsgi_application()
#
#
# django_asgi_app = get_asgi_application()
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django_private_chat2 import urls
# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": AuthMiddlewareStack(
#         URLRouter(urls.websocket_urlpatterns)
#     ),
# })

# import os
#
# import django
# from channels.http import AsgiHandler
# from channels.routing import ProtocolTypeRouter
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# django.setup()
#
# application = ProtocolTypeRouter({
#   "http": AsgiHandler(),
#   # Just HTTP for now. (We can add other protocols later.)
# })

# django_asgi_app = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django_private_chat2 import urls
# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": AuthMiddlewareStack(
#         URLRouter(urls.websocket_urlpatterns)
#     ),
# })

import os

import django
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
         URLRouter(urls.websocket_urlpatterns)
     ),
})
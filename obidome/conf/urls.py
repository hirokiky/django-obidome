from django.conf.urls import url, include as django_include


def include(arg, wrapper, namespace=None, app_name=None):
    """
    Extension of django.conf.urls.include to apply decorators
    to all view callables in module provided by arg.
    """
    mod, app_name, namespace = django_include(
        arg,
        app_name=app_name,
        namespace=namespace
    )
    return decorated_urlmodule(mod, wrapper), app_name, namespace


def decorated_urlmodule(urlmodule, wrapper):
    if hasattr(urlmodule, 'urlpatterns') and urlmodule.urlpatterns:
        patterns = urlmodule.urlpatterns
    elif isinstance(urlmodule, (list, tuple)):
        patterns = urlmodule
    else:
        patterns = []
    return [decorated_urlresolver(p, wrapper) for p in patterns]


def decorated_urlresolver(urlresolver, wrapper):
    if hasattr(urlresolver, 'url_patterns') and urlresolver.url_patterns:
        return [decorated_urlresolver(p, wrapper)
                for p in urlresolver.url_patterns]
    elif hasattr(urlresolver, 'callback') and urlresolver.callback:
        return url(
            urlresolver._regex,
            wrapper(urlresolver.callback),
            name=urlresolver.name
        )

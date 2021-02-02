import os

from aiohttp.web import Response
from lona.routing import Route, MATCH_ALL

DJANGO = False

if os.environ.get('DJANGO', '0') == '1':
    from django_project.wsgi import application
    from aiohttp_wsgi import WSGIHandler

    DJANGO = True
    wsgi_handler = WSGIHandler(application)


def routing__callback_view(request):
    return """
        <h1>Callback View</h1>
    """


def routing__http_pass_through_callback_view(request):
    return Response(
        body='<h1>Pass Through Callback View</h1>',
        content_type='text/html',
    )


routes = [
    # view types
    Route('/view-types/interactive-view/',
          'views/view_types/interactive_view.py::handle_request'),

    Route('/view-types/non-interactive-view/',
          'views/view_types/non_interactive_view.py::handle_request',
          interactive=False),

    Route('/view-types/http-pass-through/',
          'views/view_types/http_pass_through_view.py::handle_request',
          http_pass_through=True),

    Route('/view-types/multi-user-view/',
          'views/view_types/multi_user_view.py::handle_request'),

    Route('/view-types/daemonized-view/<name>/',
          'views/view_types/daemonized_view.py::handle_request'),

    Route('/view-types/daemonized-view/',
          'views/view_types/daemonized_view.py::handle_request'),

    Route('/view-types/class-based-view/',
          'views/view_types/class_based_view.py::ClassBasedView'),

    Route('/view-types/async-view/',
          'views/view_types/async_view.py::AsyncView'),

    # response types
    Route('/response-types/template-response/',
          'views/response_types/template_response.py::handle_request'),

    Route('/response-types/file-response/',
          'views/response_types/file_response.py::handle_request',
          interactive=False),

    Route('/response-types/json-response/',
          'views/response_types/json_response.py::handle_request',
          interactive=False),

    Route('/response-types/redirect/',
          'views/response_types/redirect.py::handle_request'),

    Route('/response-types/http-redirect/',
          'views/response_types/http_redirect.py::handle_request'),

    # error types
    Route('/error-types/interactive-500/',
          'views/error_types/interactive_500.py::handle_request'),

    Route('/error-types/non-interactive-500/',
          'views/error_types/non_interactive_500.py::handle_request',
          interactive=False),

    Route(
        '/error-types/non-interactive-feature-error/',
        'views/error_types/non_interactive_feature_error.py::handle_request',
    ),

    # crashes
    Route('/crashes/process-connection/',
          'views/crashes/middlewares.py::handle_request'),

    Route('/crashes/process-request/',
          'views/crashes/middlewares.py::handle_request'),

    Route('/crashes/response-dict/',
          'views/crashes/response_dict.py::handle_request'),

    Route('/crashes/input-events/',
          'views/crashes/input_events.py::CrashingEventHandler'),

    Route('/crashes/handle-500/',
          'views/crashes/handle_500.py::handle_request'),

    # routing
    Route('/routing/url-args/<a:[^/]+>/<b:[^/]+>/<c:[^/]+>/',
          'views/routing/url_args.py::handle_request'),

    Route('/routing/callback-view/', routing__callback_view),

    Route('/routing/http-pass-through-callback-view/',
          routing__http_pass_through_callback_view,
          http_pass_through=True),

    # events
    Route('/events/click-events/',
          'views/events/click_events.py::handle_request'),

    Route('/events/change-events/',
          'views/events/change_events.py::handle_request'),

    Route('/events/non-node-events/',
          'views/events/non_node_events.py::handle_request'),

    Route('/events/widget-event-handler/',
          'views/events/widget_event_handler.py::handle_request'),

    Route('/events/class-based-view/',
          'views/events/class_based_view.py::ClassBasedView'),

    Route('/events/event-bubbling/',
          'views/events/event_bubbling.py::View'),

    Route('/events/data-binding/',
          'views/events/data_binding.py::handle_request'),

    # locking
    Route('/locking/html-tree/',
          'views/locking/html_tree_locking.py::LockingView'),

    Route('/locking/server-state/',
          'views/locking/server_state_locking.py::LockingView'),

    # window actions
    Route('/window-actions/set-title/',
          'views/window_actions/set_title.py::handle_request'),

    # frontend
    Route('/frontend/widget-data/',
          'views/frontend/widget_data.py::handle_request'),

    Route('/frontend/custom-event/',
          'views/frontend/custom_event.py::handle_request'),

    Route('/frontend/custom-messages/',
          'views/frontend/custom_messages.py::handle_request'),

    # contrib
    Route('/contrib/chart-js/',
          'views/contrib/chartjs.py::handle_request'),

    # home
    Route('/', 'views/home.py::home'),
]


if DJANGO:
    routes += [
        Route('/django/login-required/',
              'views/django/permission_views.py::django_login_required'),

        Route('/django/template-based-form/',
              'views/django/template_based_form.py::handle_request'),

        Route('/django/node-based-form/',
              'views/django/node_based_form.py::handle_request'),

        Route('/django/data-binding-form/',
              'views/django/data_binding_form.py::handle_request'),

        Route(MATCH_ALL, wsgi_handler, http_pass_through=True),
    ]

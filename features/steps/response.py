from behave import given, when, then

ERROR_STATUS_CODE = 'response code was {status_code}'

@then('the response code should be {response_code}')
def step_impl(context, response_code):
    response_code = int(response_code)

    assert context.response.status_code == response_code, \
            ERROR_STATUS_CODE.format(status_code=context.response.status_code)
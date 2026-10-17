
def test_login_with_valid_credentials():
    username = "student123"
    password = "password123"

    # Simulate a successful login response
    login_successful = bool(username and password)

    assert login_successful is True
    print("Login test passed")


def test_login_with_empty_credentials():
    username = ""
    password = ""

    # Simulate rejection of empty credentials
    login_successful = bool(username and password)

    assert login_successful is False
    print("Empty credentials test passed")

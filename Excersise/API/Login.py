import creds
import pytest

expected_output = "Invalid Username or Password"
@pytest.mark.parametrize("Input, expected_output",
                         [
                             ("jay.patel8161@gmail.com", "Test1234"),
                             ("xyz@gmail.com", "897657#*"),
                             ("shipt@gmail.com", "987654")
                         ]
                         )

def test_wrong_cred(input, expected_output):

    output1 = credentials.wrong_cred(input)

    assert output1 == "Invalid Username or Password"

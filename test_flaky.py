import random
import time

def test_flaky_user_login():
    # This test will fail roughly 50% of the time
    if random.choice([True, False]):
        assert True
    else:
        assert False

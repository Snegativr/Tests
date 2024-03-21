import pytest
import time
from LR5 import func

@pytest.fixture
def init_data():
    return True, 3

@pytest.mark.parametrize("par2, par3, expected_result", [
    (True, 3, 0),
    (True, 33, 24150),
    (True, 333, 43812750),
    (False, 3, 0),
    (False, 33, 0),
    (False, 333, 0)
])
def test_func(par2, par3, expected_result):
    assert func(par2, par3) == expected_result

def test_func_with_exception():
    with pytest.raises(TypeError):
        func("string", 3)

def test_func_execution_time():
    start_time = time.time()
    func(True, 33)
    end_time = time.time()
    execution_time = end_time - start_time
    assert execution_time < 1 

if __name__ == '__main__':
    unittest.main()
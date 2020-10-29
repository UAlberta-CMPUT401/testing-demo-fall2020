from mock import patch
from mymath import MyMath



'''
Suppose we want to test complicated_function(). Since it calls
bad_random(), this is not trivial
How do we even know what bad_random will return? It's random,
and we don't have the datafile
The solution is to patch bad_random() with some return value
'''
@patch('mymath.MyMath.bad_random')
def test_complicated_function(bad_random):
    bad_random.return_value = 42
    myMath = MyMath()
    result = myMath.complicated_function(2)

    assert result[0] == 21
    assert result[1] == 0

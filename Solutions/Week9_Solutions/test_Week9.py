# Import all functions from Week 9
from Week9 import *

def test_1():

    test_list = [1,2,3,3,3,4,5] 

    assert exercise_1(test_list) == (3, 3, 21, 3)


# Write some tests for the rest of the functions in Week9.py!

def test_2():

    assert exercise_2("Hello", "World") == "HelloWorld"


def test_3():

    exercise_df = exercise_3([1,2,3],[4,5,6],[7,8,9])
    answer_df = pd.DataFrame(
        data = np.array([[1,2,3],[4,5,6],[7,8,9]]).T
    )

    assert all(exercise_df) == all(answer_df)


def test_4():

    assert exercise_4([1,2,3,4,5]) == [1,3,5,7,9]


def test_5():

    assert exercise_5([0, 1, 2, 3, 4, 5]) == [0, 1, 3, 6, 10, 15]

import gauss_jordan_method.gauss_jordan as gj


def test_slae():
    """Тест СЛАУ"""
    assert gj.main([[2, 3], [4, 3]], [2, 7]) == [2.5, -1]


def test_slae2():
    """Тест СЛАУ"""
    assert gj.main([[-1, 2, 6], [3, -6, 0], [1, 0, 6]], [15, -9, 5]) == [-7, -2, 2]


def test_slae3():
    """Тест СЛАУ"""
    assert gj.main([[4, -7, 8], [2, -4, 5], [-3, 11, 1]], [-23, -13, 16]) == [-2, 1, -1]


def test_slae4():
    """Тест СЛАУ"""
    assert gj.main([[1, 2, 3, -2], [2, 4, -2, -3], [3, 2, -1, 2], [2, -3, 2, 1]], [6, 18, 4, -8]) == [1, 2, -1, -2]


def test_slae5():
    """Тест СЛАУ"""
    assert gj.main([[1, 2, 3], [4, 5, 6], [7, 8, 0]], [5, 8, 2]) == [-2, 2, 1]

# test_lab.py

import lab

def test_cube():
    cube1 = lab.cube(2)
    assert cube1 == 8
    
if __name__ == '__main__':
    test_cube()
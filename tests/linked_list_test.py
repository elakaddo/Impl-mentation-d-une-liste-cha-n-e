import unittest, sys
from hamcrest import *
sys.path.append("samples/")
from linkedList import *


class LinkedListTest(unittest.TestCase) :
    def test_isEmpty(self):
        l = LinkedList()
        assert_that(True, equal_to(l.is_empty()))

    def test_is_added_in_last(self):
        l = LinkedList()
        assert_that(None, equal_to(l.getLastElement()))

        l.addLast(2)
        assert_that(2, equal_to(l.getLastElement()))

        l.addLast(3)
        assert_that(3, equal_to(l.getLastElement()))
    
    def test_is_added_in_first(self):
        #Test when list is empty
        l = LinkedList()
        assert_that(None, equal_to(l.getFirstElement()))

        #Test when list is not empty
        l.addFirst(2)
        assert_that(2, equal_to(l.getFirstElement()))


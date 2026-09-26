from tracker import Tracker

def test_add_and_total():
    tr = Tracker()
    tr.add("buy milk", 30.0)
    tr.add("bus ticket", 10.0)
    assert tr.total_cost() == 40.0

def test_complete():
    tr = Tracker()
    tr.add("write report")
    assert tr.complete("write report") is True
    assert tr.outstanding() == []
def test_average_empty():
    from tracker import Tracker
    assert Tracker().average_cost() == 0.0
    
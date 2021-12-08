import pytest

from component import Component


def test_component(mocker):
	def fake_dbl_str(s):
		return s+"42"
	# mocker.patch('component.SubComponent.double_str', fake_dbl_str)
	mock_sub = mocker.Mock()
	mock_sub.double_str = fake_dbl_str
	c = Component(mock_sub)
	assert c.method('toto') == 'toto42'
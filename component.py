from subcomponent import SubComponent

class Component:
	def __init__(self, subcomponent: SubComponent):
		self.subcomponent = subcomponent

	def method(self, s: str) -> str:
		return self.subcomponent.double_str(s)
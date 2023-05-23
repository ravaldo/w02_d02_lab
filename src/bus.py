
class Bus:
	def __init__(self, number, dest):
		self.route_number = number
		self.destination = dest
		self.passengers = []
		
	def drive(self):
		return "Brum brum"
		
	def pick_up(self, passenger):
		self.passengers.append(passenger)
		
	def drop_off(self, passenger):
		self.passengers.remove(passenger)
	
	def passenger_count(self):
		return len(self.passengers)
	
	def empty_bus(self):
		self.passengers = []
	
	def pick_up_from_stop(self, busstop):
		self.passengers.extend(busstop.queue)
		busstop.clear_queue()
		
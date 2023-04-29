import os
import sys
import tkinter
import serial


cadets = {}


class Cadet():
	def __init__(self, name, rank, cadet_id, card_id, issued, photo):
		self.name = name
		self.rank = rank
		self.cadet_id = cadet_id 
		self.card_id = card_id
		self.qsm_id = len(cadets)
		self.issued = []
		self.photo = photo


class Item():
	def __init__(self, name, type):
		pass


def create_cadet(name, rank, cadet_id, card_id, issued, photo):
	new_cadet = Cadet(name, rank, cadet_id, card_id, issued, photo)

	cadets[cadet_id] = new_cadet

create_cadet('DUFF', 'LCPL', 2386878, '0252345', None, None)
create_cadet('DUFFs', 'LCPLs', 23868781, '02523451', None, None)
create_cadet('DUFFd', 'LCPLd', 238687811, '02523451', None, None)
print(cadets[2386878].qsm_id)
print(cadets[23868781].qsm_id)
print(cadets[238687811].qsm_id)
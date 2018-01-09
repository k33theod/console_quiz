"""
Παιχνίδι ερωτήσεων τύπου quiz
Τίθεται μια ερώτηση την οποίο οι παίκτες απαντούν 1-1
Επιπρόσθετα οι παίχτες έχουν στη διάθεσή τους 2 βοήθειες
1η 50-50 όπου αντί για 4 παρουσιάζονται 2 πιθανές απαντήσεις οπότε έχουν 50%
πιθανότητα να κερδίσουν-χάσουν
2η Να αλλάξουν ερώτηση
Μετά το τέλος του παιχνιδιού βγαίνει το σκορ του κάθε παίκτη 10 βαθμούς
για κάθε σωστή απάντηση και 5 βαθμούς για βοήθεια που δεν χρησιμοποιήθηκε
"""

from quiz_erotiseis import questions, extra_questions
import random 

def print_full_question(question):
	"""
	Εκτυπώνει την ερώτηση και τις 4 πιθανές απαντήσεις με τη σειρά που είναι
	γραμμένες βάζοντας μπροστά τα ελληνικά κεφαλαία γράμματα Α,Β,Γ,Δ
	"""
	print(question['Ερώτηση'])
	print('A : {}\tB : {}\tΓ : {}\tΔ : {}'.format(question['Απαντήσεις'][0],
	question['Απαντήσεις'][1],question['Απαντήσεις'][2],question['Απαντήσεις'][3]) )
	
def print_50_50(question):
	"""
	Εκτυπώνει την ερώτηση με 2 πιθανές απαντήσεις
	η σωστή απάντηση διατηρεί την αντιστοίχηση στο ελληνικό γράμμα που έχει στο
	format με τις 4 απαντήσεις.
	"""
	answers=[0,1,2,3]#Τα index των απαντήσεων στην αρχική ερώτηση 
	print(question['Ερώτηση'])
	right_answer=question['Απαντήσεις'].index(question['Σωστή απάντηση'])
	answers.remove(right_answer)#αφαιρώ το index της σωστής απάντησης
	one_more=random.choice(answers)# Διαλέγω τυχαία μία άλλη απάντηση και τις τυπώνω με τι σειρά που είχαν αρχικά
	if right_answer<one_more:
		print ('{} : {}\t{}  : {}'.format(
		'ΑΒΓΔ'[right_answer],question['Απαντήσεις'][right_answer],
		'ΑΒΓΔ'[one_more], question['Απαντήσεις'][one_more]))
	else :
		print ('{} : {}\t{}  : {}'.format(
		'ΑΒΓΔ'[one_more], question['Απαντήσεις'][one_more],
		'ΑΒΓΔ'[right_answer], question['Απαντήσεις'][right_answer]))

class Paiktis:
	"""
	Η κλάσση αυτή κρατάει τα ονόματα το σκορ και τις βοήθειες των παικτών
	καθορίζει επίσης με τη μέθοδο play το gameplay 
	"""
	def __init__(self, onoma):
		"""
		Γίνεται αρχικοποίηση με το όνομα του χρήστη σκορ 0 και 2 βοήθειες
		"""
		self.onoma=onoma
		self.score=0
		self.helps_available=['50-50','Επόμενη Ερώτηση']
	
	@property
	def final_score(self):
		return self.score+5*len(self.helps_available)

	def use_50_50(self, question):
		self.helps_available.remove('50-50')
		print_50_50(question)

	def use_next_question(self, question):
		self.helps_available.remove('Επόμενη Ερώτηση')
		question=extra_questions.pop()
		print_full_question(question)
		self.play(question)
		
		
	def play(self, question):
		print(self.onoma)
		print('Διαθέσειμες Βοήθειες')
		print(self.helps_available)
		reply = input('Δώσε απάντηση : ')
		if reply  not in ['Α', 'Β', 'Γ', 'Δ', 'Β1', 'Β2']:
			print ('Πρέπει να επιλέξης μία απάντηση ή μια βοήθεια Β1 50-50 Β2 Επόμενη Ερώτηση')
			self.play(question)
		elif reply in ('Α', 'Β', 'Γ', 'Δ'):
			if question['Απαντήσεις']['ΑΒΓΔ'.index(reply)]==question['Σωστή απάντηση']:
				self.score+=10
		elif reply=='Β1' and  '50-50' in self.helps_available:
			self.use_50_50(question)
			self.play(question)
		elif reply=='Β1' and  '50-50' not in self.helps_available:
			print ('Λυπάμαι η επιλογή 50-50 δεν είναι διαθέσιμη')
			self.play(question)
		elif reply=='Β2'and 'Επόμενη Ερώτηση' in self.helps_available:
			self.use_next_question(question)
		elif reply=='Β2'and 'Επόμενη Ερώτηση' not in self.helps_available:
			print ('Λυπάμαι η επιλογή επόμενη ερώτηση δεν είναι διαθέσιμη')
			self.play(question)

def main():
	"""
	Δημιουργούμαι 3 παίκτες
	και παίζουν όλοι την ίδια ερώτηση
	Μετά από κάθε ερώτηση εκτυπώνεται το σκορ κάθε παίκτη και στο τέλος τα τελικά αποτελέσματα
	"""
	paiktis1=input('Όνομα πρώτου παίκτη : ')
	p1=Paiktis(paiktis1)
	paiktis2=input('Όνομα δεύτερου παίκτη : ')
	p2=Paiktis(paiktis2)
	paiktis3=input('Όνομα τρίτου παίκτη : ')
	p3=Paiktis(paiktis3)
	for question in questions:
		print_full_question(question)
		p1.play(question)
		p2.play(question)
		p3.play(question)
		print(p1.onoma +' : '+ str(p1.score) +' , '+p2.onoma +' : '+ str(p2.score)+' , '+p3.onoma +' : '+  str(p3.score))
	print('Τελικά αποτελέσματα')
	print(p1.onoma +' : '+ str(p1.final_score))
	print(p2.onoma +' : '+ str(p2.final_score))
	print(p3.onoma +' : '+ str(p3.final_score))
	
#116 grames 41 kenes
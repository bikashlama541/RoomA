class Question:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

questions_prompts = [
	"What colors are apple?\n (a) Red/Green\n (b) Orange",
	"What colors are bananas?\n (a) Red/Green\n (b)Yellow",
	]

questions = [
	Question(question_prompts[0], "a"),
	Question(question_prompts[1], "b"),
	]
def run_quiz(questions):
	score = 0
	for question in questions:
		answer = inputer(question.prompt)
		if answer == question.answer:
			score +=1
	print("You got", score, "out of", len(questions))

run_quiz(questions)

Questions = {

  "The Capital of Ghana": ["Accra", "Lagos", "Casablanca"
  "What Year was American Imdependence": [1776, 1778, 1867]
}


for question, alternatives in Questions:
  correct_answer = alternatives[0]
  for alternative in alternatives:
    print("--{}".format(alternative)

  print(f"{question}")
  answer = input(question)
  if answer == correct_answer:
    print ("correct"
  else:
    print(" answer is {} not {} ".format(correct_answer,answer)

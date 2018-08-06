import sys
import json
import random

if __name__ == "__main__":
    input_file = sys.argv[1]
    prediction_file = sys.argv[2]

    data = json.load(open(input_file))
    answers = [d["answer"] for d in data]
    random.shuffle(answers)
    predicts = {data[i]["id"]: answers[i] for i in range(len(answers))}

    with open(prediction_file, "w") as f:
        f.write(json.dumps(predicts, indent=True))
        f.close()

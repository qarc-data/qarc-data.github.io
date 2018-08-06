import sys
import json

if __name__ == "__main__":
    gold_file = sys.argv[1]
    output_file = sys.argv[2]

    gold_data = json.load(open(gold_file))
    predictions = [{"utterance_id": d["utterance_id"], "answer": "Yes"} for d in gold_data]
    with open(output_file, 'w') as f:
        f.write(json.dumps(predictions, indent=True))
        f.close()
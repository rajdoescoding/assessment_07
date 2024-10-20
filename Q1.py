# Define the knowledge base as a nested dictionary
K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}

def decision_tree(node):
    if isinstance(node, dict):
        question = list(node.keys())[0]
        print(question)
        
        answer = input("Answer (Yes/No): ").strip().capitalize()
        
        if answer in node[question]:
            return decision_tree(node[question][answer])
        else:
            print("Invalid answer. Please respond with 'Yes' or 'No'.")
            return decision_tree(node)
    else:
        
        print(node)

if __name__ == "__main__":
    print("Computer Troubleshooting Decision Tree")
    decision_tree(K_Base)
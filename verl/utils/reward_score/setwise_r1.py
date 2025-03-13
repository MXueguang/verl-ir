import re
import random


def extract_solution(solution_str, method='strict'):
    # define re to extract content in the last boxed of \\boxed{...}
    boxed_re = re.compile(r"\\boxed{([^}]*)}")
    boxed_str = boxed_re.findall(solution_str)
    if len(boxed_str) > 0:
        return boxed_str[-1].replace('[', '').replace(']', '')
    else:
        return None


def compute_score(solution_str, ground_truth, method='strict', format_score=0., score=1.):
    answer = extract_solution(solution_str=solution_str, method=method)
    score = 0
    if (answer is None) or (not answer.isdigit()):
        score -= 0.5
    elif answer == ground_truth:
        score += 1

    # in random 5% of the cases, print the solution and the ground truth
    if random.random() < 0.05:
        print(f"###[Solution]\n{answer}\n\nGround Truth: {ground_truth}\n###")
    return score
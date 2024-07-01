import cv2

# all possible cases
rock_win_cases = [["Rock", "Scissors"], ["Scissors", "Rock"]]
scissor_win_cases = [["Paper", "Scissors"], ["Scissors", "Paper"]]
paper_win_cases = [["Paper", "Rock"], ["Rock", "Paper"]]
tie_cases = [["Rock", "Rock"], ["Paper", "Paper"], ["Scissors", "Scissors"]]

# win decide function
def winner_decide(classes_detected, frame, rows, font=cv2.FONT_HERSHEY_TRIPLEX, color=(0, 30, 255), thickness=2):
    """Determine the winner of the game based on the classes detected.

    Args:
        classes_detected (list): A list of strings representing the classes detected.
        frame (np.ndarray): The frame to write the winner text on.
        rows (int): The number of rows in the frame.
        font (cv2.FONT_HERSHEY_TRIPLEX): The font to use for drawing the text.
        color (tuple, optional): The color of the text. Defaults to (0, 30, 255).
        thickness (int, optional): The thickness of the text. Defaults to 2.

    Returns:
        str or None: The winner of the game, or None if there is no winner or too many players.
    """
    # If there are two classes detected, determine the winner based on the game rules.
    if len(classes_detected) == 2:
        if classes_detected == ["Rock", "Scissors"] or classes_detected == ["Scissors", "Rock"]:
            cv2.putText(frame, "Rock Wins", (int(rows / 2) - 80, 20), font, 1, color, thickness)
            winner = "Rock"
        elif classes_detected == ["Paper", "Scissors"] or classes_detected == ["Scissors", "Paper"]:
            cv2.putText(frame, "Scissors Wins", (int(rows / 2) - 80, 20), font, 1, color, thickness)
            winner = "Scissors"
        elif classes_detected == ["Paper", "Rock"] or classes_detected == ["Rock", "Paper"]:
            cv2.putText(frame, "Paper Wins", (int(rows / 2) - 80, 20), font, 1, color, thickness)
            winner = "Paper"
        else:
            # If the classes are not one of the winning cases, it's a tie.
            cv2.putText(frame, "Tie", (int(rows / 2) - 20, 20), font, 1, color, thickness)
            winner = None
    elif len(classes_detected) > 2:
        # If there are more than two classes detected, it's too many players.
        cv2.putText(frame, "Too Many Players", (int(rows / 2) - 80, 20), font, 1, color, thickness)
        winner = None
    elif len(classes_detected) < 2:
        # If there is only one class detected or no classes detected, it's not enough players.
        cv2.putText(frame, "At least Two Players Required", (int(rows / 2) - 120, 20), font, 1, color, thickness)
        winner = None

    return winner


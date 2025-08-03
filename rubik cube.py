import matplotlib.pyplot as plt
import os

# Map letters to colors
color_code = {
    'W': 'white',
    'Y': 'yellow',
    'R': 'red',
    'O': 'orange',
    'B': 'blue',
    'G': 'green'
}

face_order = ['U', 'R', 'F', 'D', 'L', 'B']

# Parse input string into cube dictionary
def parse_cube_input(cube_string):
    if len(cube_string) == 54:
        size = 3
    elif len(cube_string) == 24:
        size = 2
    else:
        raise ValueError("Input must be 24 (2x2) or 54 (3x3) characters long.")

    state = {}
    idx = 0
    for face in face_order:
        face_matrix = []
        for _ in range(size):
            row = [color_code[cube_string[idx + i]] for i in range(size)]
            face_matrix.append(row)
            idx += size
        state[face] = face_matrix
    return state, size

# Get solved cube state
def get_solved_state(size):
    face_colors = {
        'U': 'white',
        'D': 'yellow',
        'F': 'green',
        'B': 'blue',
        'L': 'orange',
        'R': 'red'
    }
    return {face: [[face_colors[face]] * size for _ in range(size)] for face in face_colors}

# Create gradual solver visualization
def simple_solver_steps(scrambled, solved, steps=6):
    result = []
    current = scrambled.copy()
    size = len(current['U'])
    for i in range(1, steps + 1):
        intermediate = {}
        for face in current:
            intermediate[face] = [
                [
                    solved[face][r][c] if (r + c) % steps < i else current[face][r][c]
                    for c in range(size)
                ]
                for r in range(size)
            ]
        result.append(intermediate)
        current = intermediate
        if intermediate == solved:
            break
    return result

# Draw full cube net
def draw_cube(state, size, title=None, save_as_image=False, step_num=0):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis('off')

    # Helper: draw one face at offset
    def draw_face(face, x_offset, y_offset):
        for i in range(size):
            for j in range(size):
                color = state[face][i][j]
                square = plt.Rectangle((x_offset + j, y_offset - i), 1, 1,
                                       facecolor=color, edgecolor='black')
                ax.add_patch(square)

    # Layout:
    #        U
    #  L  F  R  B
    #        D
    draw_face('U', size, 3 * size)
    draw_face('L', 0, 2 * size)
    draw_face('F', size, 2 * size)
    draw_face('R', 2 * size, 2 * size)
    draw_face('B', 3 * size, 2 * size)
    draw_face('D', size, size)

    ax.set_xlim(0, 4 * size)
    ax.set_ylim(0, 4 * size)
    ax.set_aspect('equal')
    if title:
        plt.title(title)
    plt.tight_layout()

    if save_as_image:
        os.makedirs("cube_steps", exist_ok=True)
        plt.savefig(f"cube_steps/step_{step_num}.png")
    plt.show()

# =================== MAIN ===================
user_input = input("Enter the cube string (24 for 2x2, 54 for 3x3) using W, Y, R, O, B, G (URFDLB order): ").upper()

scrambled_state, cube_size = parse_cube_input(user_input)
solved_state = get_solved_state(cube_size)
steps = simple_solver_steps(scrambled_state, solved_state)

for idx, step in enumerate(steps):
    draw_cube(step, cube_size, title=f"Step {idx + 1}", save_as_image=True, step_num=idx + 1)
    if step == solved_state:
        print(f"✅ Cube solved in {idx + 1} steps.")
        break

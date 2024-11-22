class TreeNode:
    def __init__(self, content=""):
        self.content = content.strip()
        self.children = []

    def __repr__(self, level=0):
        indent = " " * (level * 4)
        result = f"{indent}{self.content}\n"
        for child in self.children:
            result += child.__repr__(level + 1)
        return result


def parse_tree_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    stack = []
    root = TreeNode("root")
    current_node = root
    buffer = ""

    for char in data:
        if char == "{":
            # Cria um novo nó com o conteúdo atual do buffer
            if buffer.strip():
                new_node = TreeNode(buffer)
                current_node.children.append(new_node)
                stack.append(current_node)
                current_node = new_node
            buffer = ""
        elif char == "}":
            # Finaliza o conteúdo do nó atual
            if buffer.strip():
                current_node.children.append(TreeNode(buffer))
            buffer = ""
            if stack:
                current_node = stack.pop()
        else:
            buffer += char

    return root


def main():
    file_name = input("Enter the name of the file to load: ")

    try:
        tree = parse_tree_from_file(file_name)
        print("\nTree structure:")
        print(tree)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()


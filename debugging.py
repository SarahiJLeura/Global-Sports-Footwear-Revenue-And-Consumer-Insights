import nbformat

nb = nbformat.read("Global_Sports_Footwear_Analysis.ipynb", as_version=4)

for i, cell in enumerate(nb.cells):
    if cell.cell_type == "code":
        outputs = cell.get("outputs", [])
        if outputs:
            print(f"Cell {i}: {len(outputs)} outputs")
            for out in outputs:
                if "data" in out:
                    print("  MIME types:", list(out["data"].keys()))
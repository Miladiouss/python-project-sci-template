# Python Project Blueprint for Scientists

## This project

This is a very light Python project blueprint (and a tutorial) intended for intermediate developers and does not include the infra structure necessary for professional product delivery. This is ideal for personal small projects or for groups of one to three people, helping you keep your code organized. For more advanced projects, consider using Cookiecutter.

Note: This is still under development and I appreciate your comments and feedback.

### Data

The structure you see here, is ideal for scientific experiments where inputs and output go under `data/` where it will be ignored by git.

### Documents

You can put your notes, papers, and PDFs under `docs/`. The assumption is that you will not have auto-generated documentation (using Sphinx), but if you do, it belongs to this directory and should be kept separate from informal documents and references.

### Sandbox

`sandbox` is where you do your everyday work: developing new code, making new plots, and running tests. Speaking of plots, they can be saved at `data/figures/`.
Once you have some code with structure, you can move it to `py_src/pkg1/my_module.py` so you can easily import your classes and functions.

### Jupyter and IPython Notebooks

If you find yourself using Jupyter notebooks, consider creating a new directory named `notebook/`. However, I advice against using Jupyter notebooks for development purposes since <kbd>Shift</kbd>+<kbd>Enter</kbd> in modern editors can run your code and show your plots on a side panel ([see this for example](https://code.visualstudio.com/docs/python/jupyter-support)).

### Automated unit tests and manual proof of concepts

`test/` is designated for automated tests by **pytest**. For manual validation of your logic, consider placing your tests alongside with your code so you can import them and help future users to understand how your code works.

## To get started

1. `git clone` this repo.
   1. Rename the repo directory.
   2. Delete the `.git` directory.
2. Rename `pkg1/` under `py_src/` to your desired name. This name is how you can import you modules the same way you import `numpy` or `pandas`. Follow the [PEP8 naming convention](https://www.python.org/dev/peps/pep-0008/#package-and-module-names).
3. Add your information to `setup.py`. The template is minimal but you can add your email address, links, requirements, etc. If you are planning to put this on a public repository, you must add a license so others can use your code.
4. By running `pip install -e .` in the same directory, you can edit your code without the need to re-install it again.
5. Whether you are in this repo or using your package externally, you can use `from pkg1 import add_one` to import modules. Consider placing local packages before other dependencies such as NumPy or Pandas for better clarity.
6. Code development starts in `sandbox/`. Code freely. Once the structure of your code is clear, clean it up and place it in a module such as `py_src/pkg1/my_module.py`.

## Recommended tools and packages

I highly recommend using VSCode with the Python extension. I discourage you from using Jupyter notebook as it prevents you from developing more advanced code. However, Jupyter may be an ideal medium for presentation purposes.

Here is a list of packages that I often use. It is a good software design principle to use Pathlib and YAML although you can get by without using them. Pathlib is for path management and YAML is a human-readable data-serialization language. Say your code needs a list of masses of elementary particles. This goes in a YAML file and not in your source code.

Must use:

* **NumPy** for numerical calculations
* **Pandas** for handling dataframes (Spreadsheet in Python).
* **Plotly** for 2D and 3D plots (My opinion after 5 years and as professional data visualizer: Matplotlib is not user friendly)

* **Pathlib** for working with paths, directories, and files.
* **Yaml** for configurations and data representation. Please don't assign values for external parameters in your code.

Use is based on project:

* **PyTorch** for machine learning and GPU/CPU acceleration (**TensorFlow** is for engineers)
* **Ray** for parallel and distributed computing
* **AstroPy** for working with coordinate systems, units, everything astrophysicist have to deal with.
* **scikit-learn** for simple and efficient tools for predictive data analysis.
* **SciPy** for routine scientific calculations
* **SymPy** for symbolic calculations
* A full list coming soon ...

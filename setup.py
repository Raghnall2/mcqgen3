from setuptools import setup, find_packages
setup(
    packages = find_packages(),
    name = 'mcqgenerator',
    version='0.0.1', 
    author='Raghnall Marie Justin',
    author_email= 'raghnall2509@gmail.com',
    install_requires = [
       'openai',
       'langchain',
       'python-dotenv',
       'streamlit',
       'PyPDF2'
    ],
)
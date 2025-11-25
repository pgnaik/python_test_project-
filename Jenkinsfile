pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/pgnaik/python_test_project-.git'
            }
        }

        stage('Run Program') {
            steps {
                bat 'C:\\Users\\USER\\anaconda3\\python.exe atm.py'
            }
        }

        stage('Test') {
            steps {
                // Option A: module name
                bat 'C:\\Users\\USER\\anaconda3\\python.exe -m unittest test_atm'

                // OR Option B (discovery, if you add more tests later):
                // bat 'C:\\Users\\USER\\anaconda3\\python.exe -m unittest discover -p "test_*.py"'
            }
        }
    }
}

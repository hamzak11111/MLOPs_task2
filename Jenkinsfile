pipeline {
    agent any
    environment {
        MY_VARIABLE = 'variable changed'
    }

    stages {
        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest test.py'
            }
        }
        stage('Deploy') {
            steps {
                bat 'echo "Application deployed"' 
            }
        }
    }
}

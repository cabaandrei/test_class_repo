pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello there! This is just some test pipeline.'
                git 'https://github.com/cabaandrei/test_class_repo'
                bat 'dir'
                bat 'python some_test.py'
            }
        }
    }
}
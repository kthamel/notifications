pipeline {
    agent {label 'devops'}

    stages {
        stage('Create Artifact') {
            steps {
                    sh '''
                    zip notification.zip notification.py
                    '''
                }  
            }

        stage('Push Artifact') {
            steps {
                    sh '''
                    aws s3 cp notification.zip s3://kthamel-lambdas
                    '''
                }
            }

        stage('TF Apply') {
            input {
            message "Are you sure to do that?"
                id "InputMsg"
            }
            steps {
                dir('vpc_configuration') {
                    sh '''
                    echo Deploying into develop!!!
                    '''
                }
            }          
        }
    }
}
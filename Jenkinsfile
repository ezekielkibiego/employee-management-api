pipeline {
    agent any
    
    environment {
        // Define environment variables
        DOCKER_IMAGE = 'flask-app'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git repository
                git 'https://github.com/ezekielkibiego/employee-management-api.git'
            }
        }
        
        stage('Build') {
            steps {
                // Build the Docker image
                script {
                    docker.build(env.DOCKER_IMAGE)
                }
            }
        }
        
        stage('Test') {
            steps {
                // Run tests inside the Docker container
                script {
                    docker.image(env.DOCKER_IMAGE).run('--rm', 'pytest')
                }
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the Docker container
                script {
                    docker.image(env.DOCKER_IMAGE).run('-d', '-p', '5000:5000', '--name', 'app-container')
                }
            }
        }
    }
    
    post {
        success {
            // Post-build actions for success
            echo 'Build and deployment successful!'
        }
        failure {
            // Post-build actions for failure
            echo 'Build or deployment failed!'
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Test'){
            steps{
                sh 'chmod +x ./scripts/test.sh'
                sh './scripts/test.sh'
            }
        }

        stage('Ansible'){
            steps{
                sh 'chmod +x ./scripts/ansible.sh'
                sh './scripts/ansible.sh'
            }
        }
        stage('Deploy'){
            steps{
                sh 'chmod +x ./scripts/deploy.sh'
                sh './scripts/deploy.sh'
            }
        }                   
    }
}

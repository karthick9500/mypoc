pipeline {

agent {
        docker {
            image 'node:6-alpine'
            args '-p 3000:3000'
        }
    }
  
   parameters {
        string(name: 'Environemnt', defaultValue: 'dev', description: 'Enter the Environment name')
    }
  
  
environment {
    DOCKER_COMMON_CREDS = credentials('a05e481d-4987-4a51-8569-41fc1a47e11e')
}

  stages {
    
    
    // Stage 1
    stage("Init"){
       steps
      {
        sh 'echo "Initialize"'
        sh 'docker login -u $DOCKER_COMMON_CREDS_USR -p $DOCKER_COMMON_CREDS_PSW'
      }
    }
    
    // Stage2
    
    stage("Build"){
       steps
      {
        sh 'docker build .'
      }
    }
    
    //
    
    
    

  }
        
        
        
        
  post {
        failure {
            script {
                // CHANGE_ID is set only for pull requests, so it is safe to access the pullRequest global variable
                if (env.CHANGE_ID) {
                    pullRequest.addLabel('Build Failed')
                }
            }
        }
        success {
            script {
                // CHANGE_ID is set only for pull requests, so it is safe to access the pullRequest global variable
                if (env.CHANGE_ID) {
                    pullRequest.addLabel('Build Success')
                }
            }
        }
    }


}

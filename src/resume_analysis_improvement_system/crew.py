import os
import json
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapeWebsiteTool
)


from pydantic import BaseModel
from jambo import SchemaConverter

@CrewBase
class ResumeAnalysisImprovementSystemCrew:
    """ResumeAnalysisImprovementSystem crew"""

    
    @agent
    def resume_feedback_expert(self) -> Agent:
        
        return Agent(
            config=self.agents_config["resume_feedback_expert"],
            
            
            tools=[				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def job_posting_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["job_posting_analyst"],
            
            
            tools=[				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def resume_analysis_improvement_advisor(self) -> Agent:
        
        return Agent(
            config=self.agents_config["resume_analysis_improvement_advisor"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def cover_letter_generator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["cover_letter_generator"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def output_consolidation_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["output_consolidation_specialist"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def analyze_resume_for_feedback(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_resume_for_feedback"],
            markdown=False,
            
            
        )
    
    @task
    def analyze_job_posting_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_job_posting_requirements"],
            markdown=False,
            
            
        )
    
    @task
    def provide_resume_improvement_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["provide_resume_improvement_analysis"],
            markdown=False,
            output_json=self._load_response_format("provide_resume_improvement_analysis"),
            
        )
    
    @task
    def generate_personalized_cover_letter(self) -> Task:
        return Task(
            config=self.tasks_config["generate_personalized_cover_letter"],
            markdown=False,
            
            
        )
    
    @task
    def consolidate_final_json_output(self) -> Task:
        return Task(
            config=self.tasks_config["consolidate_final_json_output"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ResumeAnalysisImprovementSystem crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
